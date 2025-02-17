# Page Actions in IFrame

## Write, Press, Click

* Navigate to "http://the-internet.herokuapp.com/iframe"
* Clear element "#tinymce"
* Write "Clear it"
* Press "Enter"
* Click "File"
* Click "New document"
* Assert text "Clear it" does not exist

## Write, Clear

* Navigate to "http://the-internet.herokuapp.com/iframe"
* Clear element "#tinymce"
* Write "Clear it"
* Assert text "Clear it" exists on the page.

## Double Click
* Assert text "Hello World" does not exist
* Navigate to file with relative Path "/specs/data/doubleClick.html"
* Double click 

   |Type|Selector    |
   |----|------------|
   |text|Double-click|
* Assert text "Hello World" exists on the page.

## Right Click

* Navigate to relative path "./specs/data/IFrameRightClick.html"
* Right click 

   |Type|Selector   |
   |----|-----------|
   |text|Someelement|
* Click "Share On Facebook"

## Hover
* Navigate to relative path "./specs/data/IFrameCompare.html"
* Hover on element 

   |Type|Selector        |
   |----|----------------|
   |$   |".image_overlay"|
* Click "Compare"
* Hover on element 

   |Type|Selector        |
   |----|----------------|
   |$   |".image_overlay"|
* Click "Remove"

## Drag and drop
* Navigate to relative path "./specs/data/IFrameDragAndDrop.html"
* Drag ".document" and drop to ".trash"
* Drag ".document" and drop at 

   |direction|pixel|
   |---------|-----|
   |right    |300  |
   |down     |100  |
