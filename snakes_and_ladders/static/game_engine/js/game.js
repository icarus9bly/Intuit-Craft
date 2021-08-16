$(function(){
  let [rows, columns] = [10, 10]
  let container=$(".container")
  for (let i=rows;i>0;i--){
    // rows
    container.append(`<div class="row row-${i}"></div>`)
    // columns
    let row=$(`.row-${i}`)
    for (let j=0;j<columns;j++){
        row.append(`<div class="col col-no-${j+1}"> row: ${i} col: ${j+1}</div>`)
    }
  }
  console.log(container)

});
