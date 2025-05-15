import { RateMyProfessor } from "rate-my-professor-api-ts";

// accepts only 1 parameter
// which is the name of the college of interest
(async function main() {
    const rmp_instance = new RateMyProfessor("University of Michigan", "Nadiya Fink");
 
    // one asynchronous method helps retrieve information reagrding college
 
    // method takes in a boolean
    // if boolean is set to true, similar matching named college info will be returned
    // if boolean is set to false, only, the specific college will be returned
    //

    let college_info_all = await rmp_instance.get_college_info(true);
    let list_of_professors = await rmp_instance.get_professor_list();

 
    // uncomment the lines below to see the response

    console.log(college_info_all);
    console.log(list_of_professors);
 })();