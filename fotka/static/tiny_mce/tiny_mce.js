tinymce.init({
  // mode:"textareas"
  selector: 'textareas',
  menu: {
    file: { title: 'File', items: 'newdocument restoredraft | preview | print ' },
    edit: { title: 'Edit', items: 'undo redo | cut copy paste | selectall | searchreplace' },
    view: { title: 'View', items: 'code | visualaid visualchars visualblocks | spellchecker | preview fullscreen' },
    insert: { title: 'Insert', items: 'image link media template codesample inserttable | charmap emoticons hr | pagebreak nonbreaking anchor toc | insertdatetime' },
    format: { title: 'Format', items: 'bold italic underline strikethrough superscript subscript codeformat | formats blockformats fontformats fontsizes align | forecolor backcolor | removeformat' },
    tools: { title: 'Tools', items: 'spellchecker spellcheckerlanguage | code wordcount' },
    table: { title: 'Table', items: 'inserttable | cell row column | tableprops deletetable' },
    help: { title: 'Help', items: 'help' }
  }
  // height: 1500,
  // menubar: true "tools",
  // plugins: [
  //   'advlist autolink lists link image charmap print preview anchor',
  //   'searchreplace visualblocks code fullscreen',
  //   'insertdatetime media table paste code help wordcount',
  // ],
  // toolbar: 'undo redo | formatselect | ' +
  // 'bold italic backcolor | alignleft aligncenter ' +
  // 'alignright alignjustify | bullist numlist outdent indent | ' +
  // 'removeformat | help',
  // content_css: '//www.tiny.cloud/css/codepen.min.css'
});
// tinymce.init({
//   selector: 'textarea#menu2',
//   plugins: 'code',
//   menu: {
//     happy: {title: 'Happy', items: 'code'}
//   },
//   menubar: 'happy'
// });

// tinymce.init({
//   selector: "textarea",  // change this value according to your HTML
  // plugins: "code",
  // toolbar: "code",
//   menubar: "tools"
// });


