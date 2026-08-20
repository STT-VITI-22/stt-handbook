[![](/mf-name-white.png)](https://martinfowler.com)

/

# Testing Strategies in a Microservice Architecture

There has been a shift in service based architectures over the last few
years towards smaller, more focussed “micro” services. There are many
benefits with this approach such as the ability to independently
deploy, scale and maintain each component and
parallelize development across multiple teams. However,
once these additional network partitions have been introduced, the
testing strategies that applied for monolithic in process applications
need to be reconsidered.

[Toby Clemson](http://github.com/tobyclemson)

18 November 2014

[Agenda](#agenda)

[What is a microservice?](#definition)

[Microservice Anatomy](#anatomy-modules)

[Microservice Architecture](#architecture)

[Unit Testing](#testing-unit-introduction)

[Integration Testing](#testing-integration-introduction)

[Component Testing](#testing-component-introduction)

[Contract Testing](#testing-contract-introduction)

[End to End Testing](#testing-end-to-end-introduction)

[Conclusion - Options](#conclusion-options)

[Conclusion - Test Pyramid](#conclusion-test-pyramid)

[Conclusion - Summary](#conclusion-summary)

# How to use this [Infodeck](/bliki/Infodeck.html)

* Tap the info icon ![](/icons/information-2-line.svg) in the top banner to show this panel, tap it
  again to hide it.
* Move forward and backward using the arrow buttons at the top banner.
* If you’re on a touch device then a tap on the left or right will
  move backwards or forwards. Tapping elsewhere will bring up a simple
  control panel.
* If this deck has a table of contents, there will be a button on
  the top banner. Tap it to bring up a list of links to some of the
  slides in the deck. Tap it again to hide it.
* You can also use a keyboard:
  + right-arrow, down-arrow, page-down, and space move forwards.
  + left-arrow, up-arrow, page-up, and backspace move backwards
  + If you’re on a slide with many builds, then the up and down arrow
    keys will skip over the builds
  + press “g” to bring up a dialog which allows you to jump to any
    slide number. You can also do this by clicking on the page number
    on the banner.
  + press “home” to go to the first slide, “end” to the last
  + press “c” to bring up the table of contents (if there is one). Tap
    c to hide it again.

The deck should work well in the latest versions of most browsers. If
you are using Internet Explorer you will need at least version 10 to get a
proper experience.

close

Loading... please wait

Go to slide:

Previous  
(always active)

Next  
(always active)

First

Last

Go to  
slide #
