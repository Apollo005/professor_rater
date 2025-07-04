"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const rate_my_professor_api_ts_1 = require("rate-my-professor-api-ts");
// accepts only 1 parameter
// which is the name of the college of interest
(function main() {
    return __awaiter(this, void 0, void 0, function* () {
        const rmp_instance = new rate_my_professor_api_ts_1.RateMyProfessor("University of Michigan", "Nadiya Fink");
        // one asynchronous method helps retrieve information reagrding college
        // method takes in a boolean
        // if boolean is set to true, similar matching named college info will be returned
        // if boolean is set to false, only, the specific college will be returned
        //
        let college_info_all = yield rmp_instance.get_college_info(true);
        let list_of_professors = yield rmp_instance.get_professor_list();
        // uncomment the lines below to see the response
        console.log(college_info_all);
        console.log(list_of_professors);
    });
})();
