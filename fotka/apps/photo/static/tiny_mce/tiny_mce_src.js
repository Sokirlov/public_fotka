tinymce.init({
  selector: 'textarea#basic-example',
  height: 1500,
  menubar: true,
  plugins: [
    'advlist autolink lists link image charmap print preview anchor',
    'searchreplace visualblocks code fullscreen',
    'insertdatetime media table paste code help wordcount',
    'code',
  ],
  toolbar: 'undo redo | formatselect | ' +
  'bold italic backcolor | alignleft aligncenter ' +
  'alignright alignjustify | bullist numlist outdent indent | code ' +
  'removeformat | help',
  content_css: '//www.tiny.cloud/css/codepen.min.css',
  menubar: "tools",
});


// tinymce.init({
//   selector: "textarea",  // change this value according to your HTML
  // plugins: "code",
  // toolbar: "code",
//   menubar: "tools"
// });
