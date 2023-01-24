function createAnnotationCheckbox() {
  
  var form = FormApp.getActiveForm();
  var items = form.getItems();

  // Folder is shared
  var folder = DriveApp.getFolderById('1KgtqxZXuCfdqF5BpZniyAg9Iw5aWmXOM') 
  
  while(items.length > 0){
    form.deleteItem(items.pop());
  }
  
  var img = folder.getFilesByName('plants.jpg');  
  var blob = img.next().getBlob();

  form.addImageItem().setImage(blob).setTitle('We need your help to validate data we automatically extracted from random webpages with a deep learning model. This model is trained to recognize descriptive sentences about species, and in these cases about plants. We received hand-annotated species traits and now we need your help to match this ground-truth data, against our system that automatically extracted the traits from the internet.');
  
  var examples = folder.getFilesByName('top_sents_all_AllSentencesAgainstTrait_Random20Subset.csv')
  var data = examples.next().getBlob().getDataAsString();
  var lines = data.split("\n");
  var data = lines.map(function(lin){return lin.split("\t")});
  

  for (var i = 1; i < data.length -1; i++) {
    var pageOne = form.addPageBreakItem();
    
    // BASIC DATA
    var species_name = data[i][0]
    var gt_MainTrait = data[i][2]
    // Unlist the traits (can be more than 1) NOT YET WORKING INVALID FORMAT DUE TO PANDAS SAVING
    var gt_SubTrait  = data[i][3];
    // var gt_SubTrait_lst = eval(gt_SubTrait_str);
    // var gt_SubTrait = gt_SubTrait_lst.join(', ')

    // Top k predictions
    var pred_1 = data[i][4]
    var pred_2 = data[i][5]
    var pred_3 = data[i][6]
    var pred_4 = data[i][7]
    var pred_5 = data[i][8]

    // // POSSIBLE IMAGE
    // var url = data[i][9]; 
    // var blob = UrlFetchApp.fetch(url).getBlob();

    // BASIC INFORMATION
    pageOne.setTitle(
      "The next question is about the "  +
      species_name)
    pageOne.setHelpText(
      "The question is about the:\n" + gt_MainTrait +
      "\nThe hand-annotated traits are:\n" +
      gt_SubTrait
    )
    
    // // FORM TITLE
    form.setTitle(species_name)

    // PREDICTION
    var prediction_text = form.addCheckboxItem()
    prediction_text.setHelpText(
      "Can you indicate which of the sentences contain the trait described in the ground-truth data?"
    )


    prediction_text.setChoiceValues(
      [
      pred_1,
      pred_2,
      pred_3,
      pred_4,
      pred_5
      ]
      )
  

    // QUESTIONS
    var question = form.addMultipleChoiceItem();
    // question.setTitle('The species name is: ' + species_name);
    question.setHelpText(
      "Can you indicate to what extend the sentence(s) are correct?"
    )
    question.setChoiceValues([
      'Completely Correct', 
      'Somewhat Correct', 
      'A Little Bit Correct', 
      'Not Correct at all'
      ]);
    question.showOtherOption(
      false);

  }
  
}
