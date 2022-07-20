from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("DIDI8", 5, 666, 250)
        self.hero_replica = Hero("DIDI8", 5, 666, 250)
        self.strong_hero = Hero("Insomnia", 100, 6666, 500)
        self.hero_equal_strength = Hero("Zeerax", 50, 666, 250)

    def test_init(self):
        new_hero = Hero("Balance", 51, 667, 251)
        self.assertEqual("Balance", new_hero.username)
        self.assertEqual(51, new_hero.level)
        self.assertEqual(667, new_hero.health)
        self.assertEqual(251, new_hero.damage)

    def test_battle_with_same_username_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero_replica)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_self_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_health_raises(self):
        self.hero.health = 0
        self.assertEqual(0, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.strong_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_negative_health_raises(self):
        self.hero.health = -10
        self.assertEqual(-10, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.strong_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_enemy_zero_health_raises(self):
        self.hero.health = 0
        self.assertEqual(0, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.strong_hero.battle(self.hero)
        self.assertEqual("You cannot fight DIDI8. He needs to rest", str(ex.exception))

    def test_battle_with_enemy_negative_health_raises(self):
        self.hero.health = -100
        self.assertEqual(-100, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.strong_hero.battle(self.hero)
        self.assertEqual("You cannot fight DIDI8. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        actual_result = self.hero.battle(self.hero_equal_strength)
        self.assertEqual("Draw", actual_result)

    def test_battle_win(self):
        actual_result = self.strong_hero.battle(self.hero)
        self.assertEqual("You win", actual_result)
        expected_level = 101
        expected_health = 5421
        expected_damage = 505
        self.assertEqual(expected_level, self.strong_hero.level)
        self.assertEqual(expected_health, self.strong_hero.health)
        self.assertEqual(expected_damage, self.strong_hero.damage)

        self.assertLessEqual(self.hero.health, 0)

    def test_battle_lose(self):
        actual_result = self.hero.battle(self.strong_hero)
        self.assertEqual("You lose", actual_result)
        expected_level = 101
        expected_health = 5421
        expected_damage = 505
        self.assertEqual(expected_level, self.strong_hero.level)
        self.assertEqual(expected_health, self.strong_hero.health)
        self.assertEqual(expected_damage, self.strong_hero.damage)

        self.assertLessEqual(self.hero.health, 0)

    def test_str(self):
        expected_result = f"Hero DIDI8: 5 lvl\n" \
               f"Health: 666\n" \
               f"Damage: 250\n"
        actual_result = str(self.hero)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
