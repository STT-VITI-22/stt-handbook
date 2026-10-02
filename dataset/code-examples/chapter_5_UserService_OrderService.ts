// UserService та OrderService взаємодіють
// Коли користувач створює замовлення, його баланс повинен зменшитися

interface User {
    id: number;
    balance: number;
    name: string;
}

interface Order {
    id: number;
    userId: number;
    amount: number;
    status: "pending" | "completed";
}

class UserService {
    private users: Map<number, User> = new Map();

    addUser(id: number, name: string, balance: number): void {
        this.users.set(id, { id, name, balance });
    }

    getUser(id: number): User | undefined {
        return this.users.get(id);
    }

    reduceBalance(id: number, amount: number): boolean {
        const user = this.users.get(id);
        if (!user || user.balance < amount) {
            return false;
        }
        user.balance -= amount;
        return true;
    }
}

class OrderService {
    private orders: Order[] = [];
    private nextOrderId = 1;

    constructor(private userService: UserService) {}

    createOrder(userId: number, amount: number): Order | null {
        const user = this.userService.getUser(userId);
        if (!user) {
            return null;
        }

        // Спробуємо зменшити баланс користувача
        if (!this.userService.reduceBalance(userId, amount)) {
            return null; // Недостатньо коштів
        }

        // Створюємо замовлення
        const order: Order = {
            id: this.nextOrderId++,
            userId,
            amount,
            status: "completed",
        };
        this.orders.push(order);
        return order;
    }

    getOrder(id: number): Order | undefined {
        return this.orders.find((o) => o.id === id);
    }
}

// Integration Test
describe("UserService та OrderService", () => {
    let userService: UserService;
    let orderService: OrderService;

    beforeEach(() => {
        userService = new UserService();
        orderService = new OrderService(userService);
    });

    test("створення замовлення повинна зменшити баланс користувача", () => {
        // Arrange
        userService.addUser(1, "Іван", 1000);

        // Act
        const order = orderService.createOrder(1, 250);

        // Assert
        expect(order).not.toBeNull();
        expect(order?.amount).toBe(250);
        expect(userService.getUser(1)?.balance).toBe(750); // 1000 - 250
    });

    test("не повинна створити замовлення якщо недостатньо коштів", () => {
        // Arrange
        userService.addUser(1, "Марія", 100);

        // Act
        const order = orderService.createOrder(1, 250); // Більше ніж баланс

        // Assert
        expect(order).toBeNull();
        expect(userService.getUser(1)?.balance).toBe(100); // Баланс не змінився
    });

    test("не повинна створити замовлення для неіснуючого користувача", () => {
        // Act
        const order = orderService.createOrder(999, 100);

        // Assert
        expect(order).toBeNull();
    });
});
