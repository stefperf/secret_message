# secret_message
Script solving a generalization of the problem in Riddler Classic 2021-04-06 @ https://fivethirtyeight.com/features/can-you-decipher-the-secret-message/ :
finding all sets of topologically equivalent English n-grams and all topologically unique English n-grams, with reference to the given sans serif font.

Here, an English n-gram is defined as topologically unique if there is no second English n-gram with the same length and with each of its letters homeomorphic to the corresponding letter, in order by position, of the first n-gram.

It turns out that 59% of English n-grams, including the solution EUREKA encoded as YIRTHA, are unique.
