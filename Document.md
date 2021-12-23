# Locators in Selenium

APP: https://the-internet.herokuapp.com/login

Below is the list of these locators of Selenium WebDriver.

```
- ID
- Name
- Linktext
- Partial Linktext
- Tag Name
- Class Name
- DOM Locator
- CSS Selector
- Xpath
```

## ID Locator
Based on the World Wide Web Consortium(W3C) ID’s should be unique to elements and they are considered as the fastest and safest method to locate element. But unfortunately, developers may or may not follow this rule as browsers do allow bypassing this rule. Specifically, in the case of a table or list the ID’s may populate incrementally or dynamically depending upon the data, which leads to locating such elements through other means.

Example: 
    - driver.findElement(By.id("username"))
    - In case no such value matches with id, `NoSuchElementException` will be raised.

## Name Locator

An element can be defined via multiple attributes, one such is Name. Name locator in Selenium WebDriver can also be used to locate elements like ID locator. They may or may not be unique on a page, having multiple elements. In case there are elements with the same name, then the locator selects the first element with that name on the page.

Example:
    - driver.findElement(By.name("username"));
    - In case no such name matches with the defined attribute value, `NoSuchElementException` will be raised.


## DOM Locator

In document object model(DOM) we locate element in terms of DOM model. As explained above we can identify element via ID and name through methods of the DOM like ‘getElementById’ and ‘getElementsByName’. The method getElementById will locate only one element at a time, whereas the other method is used to provide an array of elements located by that name. In order to access any specified element in case of an array of elements, we can use index.

The syntax used to access id and name through DOM is:
    - document.getElementById (“id”)
    - document.getElementsByNames (“name”)[index]

Example:
    - document.getElementById (“remember”)
    - document.getElementsByNames (“remember”)[0]