import React, { useState } from "react";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import Input from "@mui/material/Input";


function AskWord(props) {
	//console.log(Math.floor(Math.random() * props.wordList.length) + 1)
	const thisWord = props.wordList[Math.floor(Math.random() * props.wordList.length) + 1]

const [kulu, setValues] = useState({
    guess: "",
    paiva: new Date(),
    summa: "",
    tyyppi: "",
    maksaja: "",
    jako: "",
    takuu: null,
    kuitti: [],
  });

  const [viesti, setViesti] = useState("");

  const muuta = (e) => {
    setValues({
      ...kulu,
      [e.target.name]: e.target.value,
    });

    setViesti("");
  };

  const muutaSumma = (e) => {
    let pilkuton = e.target.value.replace(",", ".");
    if (pilkuton === "" || !isNaN(pilkuton)) {
      setViesti("");
      setValues({
        ...kulu,
        [e.target.name]: pilkuton,
      });
    } else setViesti("Syötä numero!");
  };

  const muutaSuurella = (e) => {
    setValues({
      ...kulu,
      [e.target.name]: e.target.value.toUpperCase(),
    });

    setViesti("");
  };

  const muutaKuitti = (e) => {
    setValues({
      ...kulu,
      kuitti: e.target.files[0],
    });

    setViesti("");
  };
  const lisaaKulu = (e) => {
    e.preventDefault();
    if (
      kulu.guess !== "" &&
      kulu.paiva !== "" &&
      kulu.summa !== "" &&
      kulu.tyyppi !== "" &&
      kulu.maksaja !== ""
    ) {
      //console.log(kulu);
      setViesti("Lisättiin");
      setValues({
        guess: "",
        paiva: new Date(),
        summa: "",
        tyyppi: null,
        maksaja: null,
        jako: "",
        takuu: null,
        kuitti: "",
      });
    } else {
      setViesti(
        "Täytä"
      );
    }
  };

  const tyhjenna = (e) => {
    setValues({
      guess: "",
      paiva: new Date(),
      summa: "",
      tyyppi: "",
      maksaja: "",
      jako: "",
      takuu: null,
      kuitti: "",
    });

    setViesti("");
  };

  let kuittiNimi = "";
  if (kulu.kuitti !== null) {
    kuittiNimi = kulu.kuitti.name;
  }

  return (
    <Paper sx={{ padding: "10px", margin: "10px" }}>
          <Box
            component="form"
            sx={{ "& .MuiTextField-root": { marginBottom: 2 }, padding: 2 }}
          >
            <TextField
              label="Guess"
              name="guess"
              value={kulu.guess}
              onChange={(e) => muutaSuurella(e)}
              required
              fullWidth
              autoFocus
            />
    
     
              <Box sx={{ textAlign: "left" }}>
              <Button
                onClick={(e) => lisaaKulu(e)}
                variant="contained"
                sx={{ marginRight: 3 }}
                
              >
                Guess
              </Button>
            </Box>
          </Box>
    
          <Typography sx={{ marginTop: 3 }}>{thisWord.word}</Typography>
        </Paper>
  );
}

export default AskWord;
