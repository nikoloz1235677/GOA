fun main() {
    val num1 = listOf(1, 2, 3, 4, 5)
    println(num1.map { it * 2 })
}



fun main() {
    val num1 = listOf(1, 2, 3, 4, 5)
    println(num1.map { it + 1 })
}




fun numm() { 
    val num1 = listOf(1, 2, 3, 4, 5, 6, 7, 8)
    println(num1.filter { it % 2 == 0 })
}



fun number() {
    val num1 = listOf("car", "bmw", "a", "gg", "af")
    val n = num1.filter { it.length == 5 }
    println(n)
}