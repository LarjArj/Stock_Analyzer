const stock_info = {
    "stocks":"AAPL"
};


//get JSON stick data and output into array
function parseStockTable(){
    let stock_table = stock_info;
    let stock_array  = [];
    
    for (key in stock_table){
        stock_array.push(stock_table[key]);  
    }
    return stock_array;

}




//On button click, prepare and display infographic
(function () {
    document.getElementById("btn").addEventListener("click", processEvent);
})();


function processEvent() {
    let inputStock = processForm();
    let stocks = getRandomStock();
    let StockInfo = {};
    let factToInsert=null;
    /// hide initial form once button is clicked
    document.getElementById("stock-compare").style.display = "none";
    let counter=0;
    let idx =0;
    while  (counter<stocks.length){
        let stock;
        stock = StockInfo[counter];
       if (idx == 3){
            

        }
        else{
            counter++;
          

            stock= new StockConstructor();
            let facts = compareGetFacts(stock,inputStock);
            stock.facts=facts;
            StockInfo[animal.name]=Dino;


            let Dino_facts = animal.facts;
            factToInsert = getRandomFact(Dino_facts);
            

        }
        

        gridTile = createTile(stock,factToInsert,idx);
        document.getElementById("grid").appendChild(gridTile);
        idx++;
        

    }

}

/// Uses DOM principles to create a tile which will ultimately be 
//appended to the grid
function createTile(stock,fact,idx){

    let tileItemDiv = document.createElement("div");
    tileItemDiv.className = "grid-item";
    let StockNameDiv = document.createElement("h3");
    StockNameDiv.innerText = stock.name;
    tileItemDiv.appendChild(animalNameDiv);


    if (idx!=3){
        let stockImageDiv = document.createElement("img");
        stockImageDiv.src = stock.picture;
        tileItemDiv.appendChild(stockImageDiv)
        let stockFactDiv = document.createElement("p");
        stockFactDiv.innerText = fact;
        tileItemDiv.appendChild(stockFactDiv);
    }

    return tileItemDiv;
}

/// Processes User input and creates a Human obj
function processForm() {
    let name = document.getElementById("name").value;
   
    return new StockConstructor(tickerSymbol,averagePrice,annualizedReturn,standardDeviation);

}

function StockConstructor (tickerSymbol,averagePrice,annualizedReturn,standardDeviation) {
    this.tickerSymbol = tickerSymbol;
    this.averagePrice = averagePrice;
    this.annualizedReturn = annualizedReturn;
    this.standardDeviation = standardDeviation;

}


function getComparisons(otherStock,InputtedStock){
    let facts = [];
    facts.push(compareHeight(otherStock,InputtedStock));
    facts.push(compareWeight(otherStock,InputtedStock));
    facts.push(compareDiet(otherStock,InputtedStock));
    return facts;

}

function compareAveragePrice (otherStock,InputtedStock){
    let potentialFact;
    if (otherStock.averagePrice==InputtedStock.averagePrice){
         potentialFact ="Both "+otherStock.tickerSymbol+" and" + InputtedStock.tickerSymbol + "have the same averagePrice";
    }
    
    if (otherStock.averagePrice>InputtedStock.averagePrice){
        potentialFact = otherStock.tickerSymbol+" trades at average price of" + "more than " + InputtedStock.tickerSymbol + "price";
    }
    else{
         potentialFact = otherStock.tickerSymbol+" trades at average price of" + "less than " + InputtedStock.tickerSymbol + "price"
    }
    return potentialFact;
}

function compareVolatility (otherStock,InputtedStock){
    if (otherStock.averagePrice==InputtedStock.averagePrice){
        potentialFact ="Both "+otherStock.tickerSymbol+" and" + InputtedStock.tickerSymbol + "have the same averagePrice";
   }
   
   if (otherStock.averagePrice>InputtedStock.averagePrice){
       potentialFact = otherStock.tickerSymbol+" trades at average price of" + "more than " + InputtedStock.tickerSymbol + "price";
   }
   else{
        potentialFact = otherStock.tickerSymbol+" trades at average price of" + "less than " + InputtedStock.tickerSymbol + "price"
   }
   return potentialFact;

function compareAnnualizedReturn(otherStock,InputtedStock){
    if (otherStock.averagePrice==InputtedStock.averagePrice){
        potentialFact ="Both "+otherStock.tickerSymbol+" and" + InputtedStock.tickerSymbol + "have the same averagePrice";
   }
   
   if (otherStock.averagePrice>InputtedStock.averagePrice){
       potentialFact = otherStock.tickerSymbol+" trades at average price of" + "more than " + InputtedStock.tickerSymbol + "price";
   }
   else{
        potentialFact = otherStock.tickerSymbol+" trades at average price of" + "less than " + InputtedStock.tickerSymbol + "price"
   }
   return potentialFact;

}

function getRandomFact(facts){
    let random = getRndInteger(0,facts.length);
    swap(random,facts.length-1,facts);
    return facts.pop();
}



function getRandomStocks(){
    let Stock_list = parseStockTable();
    let output = []
    while (Stock_list.length>0){
        let random = getRndInteger(0,Dino_list.length);
        swap(random,Dino_list.length-1,Dino_list);

        let popped = Stock_list.pop();
        output.push(popped);
    }
    return output;

}
function getRndInteger(min, max) {
    return Math.floor((Math.random() * (max)) + min);
}


function test(){
    let li = [2,32,13,6,8];
    let output  =[];
    while (li.length>0){
        let random = getRndInteger(0,li.length);
        swap(random,0,li);

        let popped = li.pop();
        output.push(popped);
        
    }
    return output;
}

function swap(a,b,array){
    let temp = array[a];
    array[a] = array[b];
    array[b] = temp;



}




async function fetchText() {
    let response = await fetch();
    let data = await response.text();
    console.log(data);
}