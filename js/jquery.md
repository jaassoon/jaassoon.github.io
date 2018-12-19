jquery.md  
###### jquery
 $('#xForm').find('input').each(function(){
    if($(this).is(':radio')||$(this).is(':text')){$(this).prop('disabled', true)}})
###### jquery
$("input[id^='frontTime']").each(function(){
      $(this).closest('div').find('button').each(function(){$(this).prop('disabled', true)})})    

###### &nbsp;      

###### done().fail() is updated usage vs success
###### on() is updated usage vs .bind() event
###### removeAttr(name) .attr( attributeName, value )
###### break vs continue
return false; // break の代わり
###### addClass vs removeClass
removeAttr('readonly');
attr('readonly', 'readonly');
###### var size = Object.keys(myObj).length;
###### previous url
document.referrer
css('name',value)
str.indexOf()
if(options.callback&&$.type(options.callback) === "function")options.callback();
###### .attr vs .prop
$(".myCheckbox").attr('checked', true); // Deprecated
$(".myCheckbox").prop('checked', true);

$(要素).is(':disabled') 
$(this).text().substring(0,25);
###### $form.serializeArray() vs $form.serialize()

jquery-plugins  
DateTimePicker.pdf  
jquery - DatePicker Javascript pass array of allowed times on init - Stack Overflow.pdf  
jquery - How to allow user to select empty string on Select2 - Stack Overflow.pdf  
jQuery form autofill by Creative Area.pdf  
jQuery LoadingOverlay - Gaspare Sganga.pdf  
jQuery-form-autofill_ simply autofill an empty form with data (jQuery plugin).pdf  

jquery  
_serializeArray() _ jQuery API Documentation.pdf  
autoClear X not shown _ · Issue #982 · select2_select2 · GitHub.pdf  
Canvasイベント操作まとめ - Qiita.pdf  
How can I get the width of a table, and it's units, when it is a percentage....pdf  
How to do jquery code AFTER page loading_ - Stack Overflow.pdf  
javascript - Can I trigger date(time) picker from a function_ - Stack Overflow.pdf  
javascript - Creating an iframe with given HTML dynamically - Stack Overflow.pdf  
javascript - Disabled href tag - Stack Overflow.pdf  
javascript - Dynamically load JS inside JS - Stack Overflow.pdf  
javascript - How do I get the browser scroll position in jQuery_ - Stack Overflow.pdf  
javascript - How do I replace all line breaks in a string with _br __ tags_ - Stack Overflow.pdf  
javascript - How to pass a name to form action in thymeleaf_ - Stack Overflow.pdf  
javascript - offsetting an html anchor to adjust for fixed header - Stack Overflow.pdf  
javascript - Prompt file download with XMLHttpRequest - Stack Overflow.pdf  
javascript - Submitting the value of a disabled input field - Stack Overflow.pdf  
JavaScript Bits_ Canvas Rounded Corner Rectangles.pdf  
jquery - How to delete HTML Elements in an iFrame using JavaScript - Stack Overflow.pdf  
jquery change url of form submit - Stack Overflow.pdf  
jQuery Multiple ID selectors - Stack Overflow.pdf  
jquery ui - jQueryUI Tooltips are competing with Twitter Bootstrap - Stack Overflow.pdf  
jQuery-Timepicker-AddonにDatepickerみないなボタンをつける.pdf  
jQueryでCSSの!important指定を行う - Qiita.pdf  
jQueryを使ってselect（セレクトボックス）でplaceholderを作る！ _ Design Magazine.pdf  
php - how to set default selected for select 2 multiple choice - Stack Overflow.pdf  
Prevent button multi-clicks_.pdf  
Saving files locally using Blob and msSaveBlob (Windows).pdf  
serialization - jQuery serialize does not register checkboxes - Stack Overflow.pdf  
【jQuery】日付と時間を直感的に選択できる［DateTimePicker］が便利です。 - ONZE.pdf  
