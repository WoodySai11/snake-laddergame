// game variables
let p1Pos = 1;
let p2Pos = 1;
let currentTurn = 1; 
const end = 100;

// ladder map
const ladders = {
    8: 26, 21: 82, 43: 77, 50: 91,
    54: 93, 62: 96, 66: 87, 80: 100
};

// snake map
const snakes = {
    44: 22, 46: 5, 48: 9, 52: 11,
    55: 7, 59: 17, 64: 36, 69: 33,
    73: 1, 83: 19, 92: 51, 95: 24, 98: 28
};

// get random number between 1 and 6
function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

// update ui for active player
function updateActivePlayerUI() {
    let p1Card = document.getElementById("p1-card");
    let p2Card = document.getElementById("p2-card");
    let turnMsg = document.getElementById("turn-message"); 

    if (currentTurn === 1) {
        p1Card.classList.add("active-player");
        p2Card.classList.remove("active-player");
        turnMsg.innerText = "Player 1, it's your turn!";
    } else {
        p2Card.classList.add("active-player");
        p1Card.classList.remove("active-player");
        turnMsg.innerText = "Player 2, it's your turn!";
    }
}

// process the turn logic
function playTurn() {
    let dice = rollDice();
    let actionMsg = document.getElementById("action-message");
    let msg = `Rolled a ${dice}. `;
    
    if (currentTurn === 1) {
        p1Pos += dice;
        
        // check limits and obstacles
        if (p1Pos > end) p1Pos = end;
        if (ladders[p1Pos]) {
            p1Pos = ladders[p1Pos];
            msg += "Climbed a ladder! ";
        } else if (snakes[p1Pos]) {
            p1Pos = snakes[p1Pos];
            msg += "Bitten by a snake! ";
        }
        
        document.getElementById("p1-pos").innerText = p1Pos;
        
        if (p1Pos === end) {
            endGame("Player 1");
            return;
        }
        
        currentTurn = 2;
    } else {
        p2Pos += dice;
        
        // check limits and obstacles
        if (p2Pos > end) p2Pos = end;
        if (ladders[p2Pos]) {
            p2Pos = ladders[p2Pos];
            msg += "Climbed a ladder! ";
        } else if (snakes[p2Pos]) {
            p2Pos = snakes[p2Pos];
            msg += "Bitten by a snake! ";
        }
        
        document.getElementById("p2-pos").innerText = p2Pos;
        
        if (p2Pos === end) {
            endGame("Player 2");
            return;
        }
        
        currentTurn = 1;
    }
    
    actionMsg.innerText = msg;
    updateActivePlayerUI();
}

// handle win condition
function endGame(winner) {
    document.getElementById("turn-message").innerText = `${winner} Wins!`;
    document.getElementById("action-message").innerText = "Game Over!";
    document.getElementById("roll-btn").style.display = "none";
}

// reset variables and ui
function resetGame() {
    p1Pos = 1;
    p2Pos = 1;
    currentTurn = 1;
    
    document.getElementById("p1-pos").innerText = p1Pos;
    document.getElementById("p2-pos").innerText = p2Pos;
    document.getElementById("action-message").innerText = "Click Roll to start";
    document.getElementById("roll-btn").style.display = "block";
    
    updateActivePlayerUI();
}