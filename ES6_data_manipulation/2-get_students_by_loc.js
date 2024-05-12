export default function getStudentsByLocation(stduList, city) {
    return stduList.filter((std) => std.location === city);
}
