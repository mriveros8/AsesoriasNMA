function generatePDF(){
    const element = document.getElementById("card");

    html2pdf()
    .from(element)
    .save();
}