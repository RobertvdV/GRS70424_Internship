function createAnnotationCheckbox() {
  
  var form = FormApp.getActiveForm();
  var items = form.getItems();

  // Folder is shared
  var folder = DriveApp.getFolderById('1KgtqxZXuCfdqF5BpZniyAg9Iw5aWmXOM') 
  
  while(items.length > 0){
    form.deleteItem(items.pop());
  }
  
  form.setTitle('Plant Trait Verification');
  form.setDescription('We need your help to validate data we automatically extracted from random webpages with a deep learning model. This model is trained to recognize descriptive sentences about species, and in these cases about plants. We received hand-annotated species traits and now we need your help to match this ground-truth data, against our system that automatically extracted the traits from the internet.');
 
  var examples = folder.getFilesByName('top_sents_all_AllSentencesAgainstTrait_Random20Subset.csv')
  var data = examples.next().getBlob().getDataAsString();
  var lines = data.split("\n");
  var data = lines.map(function(lin){return lin.split("\t")});
  

  for (var i = 1; i < data.length -1; i++) {

    // BASIC DATA
    var species_name = data[i][0]
    species_name
    var gt_MainTrait = data[i][2]
    var gt_SubTrait  = data[i][3];

    // Top k predictions
    var pred_1 = data[i][4]
    var pred_2 = data[i][5]
    var pred_3 = data[i][6]
    var pred_4 = data[i][7]
    var pred_5 = data[i][8]

    var traitSentence = data[i][9]

    var pageOne = form.addPageBreakItem();
    // var choices = [
    //   sentence1.createChoice('Incorrect'),
    //   sentence1.createChoice('Correct Organ'),
    //   sentence1.createChoice('Correct Organ & Trait'),
    //   ]
    
    // BASIC INFORMATION
    pageOne.setTitle(
      "The next question is about the '" + species_name + "'.")
    pageOne.setHelpText("The hand-annotated traits is/are: " + traitSentence + ".")


    // Sentence 1
    sentence = form.addMultipleChoiceItem();
    choices = [
      sentence.createChoice('Incorrect'),
      sentence.createChoice('Correct Part/Organ'),
      sentence.createChoice('Correct Part/Organ & Trait'),
      ]
    sentence.setTitle(pred_1)
    .setChoices(choices);

    // Sentence 2
    sentence = form.addMultipleChoiceItem();
    sentence.setTitle(pred_2)
    .setChoices(choices);

    // Sentence 3
    sentence = form.addMultipleChoiceItem();
    sentence.setTitle(pred_3)
    .setChoices(choices);

    // Sentence 4
    sentence = form.addMultipleChoiceItem();
    sentence.setTitle(pred_4)
    .setChoices(choices);

    // Sentence 5
    sentence = form.addMultipleChoiceItem();
    sentence.setTitle(pred_5)
    .setChoices(choices);


  }
  
}
