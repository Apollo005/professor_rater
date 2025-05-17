import { RateMyProfessor } from "rate-my-professor-api-ts";
import fs from "fs";


// accepts only 1 parameter
// which is the name of the college of interest
(async function main() {
    const rmp_instance = new RateMyProfessor("University of Michigan");
 
    // one asynchronous method helps retrieve information reagrding college
 
    // method takes in a boolean
    // if boolean is set to true, similar matching named college info will be returned
    // if boolean is set to false, only, the specific college will be returned
    //

    let list_of_professors = await rmp_instance.get_professor_list();

 
    fs.writeFileSync(
        "professors.json",
        JSON.stringify(list_of_professors, null, 2)  // pretty print JSON with 2-space indentation
      );

    console.log("list_of_professors saved");

 })();