# -*- coding: utf-8 -*-
import pytest
from gilded_rose import Item, GildedRose


def update(items):
    GildedRose(items).update_quality()
    return items


# --- Normal items ---

class TestNormalItems:
    def test_quality_decreases_by_1(self):
        items = update([Item("Normal", sell_in=10, quality=10)])
        assert items[0].quality == 9

    def test_sell_in_decreases_by_1(self):
        items = update([Item("Normal", sell_in=10, quality=10)])
        assert items[0].sell_in == 9

    def test_quality_decreases_by_2_after_sell_date(self):
        items = update([Item("Normal", sell_in=0, quality=10)])
        assert items[0].quality == 8

    def test_quality_never_goes_below_0(self):
        items = update([Item("Normal", sell_in=10, quality=0)])
        assert items[0].quality == 0

    def test_quality_at_0_does_not_go_negative_after_sell_date(self):
        items = update([Item("Normal", sell_in=0, quality=0)])
        assert items[0].quality == 0

    def test_quality_1_after_sell_date_goes_to_0_not_negative(self):
        items = update([Item("Normal", sell_in=0, quality=1)])
        assert items[0].quality == 0


# --- Aged Brie ---

class TestAgedBrie:
    def test_quality_increases_by_1(self):
        items = update([Item("Aged Brie", sell_in=5, quality=10)])
        assert items[0].quality == 11

    def test_sell_in_decreases(self):
        items = update([Item("Aged Brie", sell_in=5, quality=10)])
        assert items[0].sell_in == 4

    def test_quality_increases_by_2_after_sell_date(self):
        items = update([Item("Aged Brie", sell_in=0, quality=10)])
        assert items[0].quality == 12

    def test_quality_never_exceeds_50(self):
        items = update([Item("Aged Brie", sell_in=5, quality=50)])
        assert items[0].quality == 50

    def test_quality_capped_at_50_after_sell_date(self):
        items = update([Item("Aged Brie", sell_in=0, quality=50)])
        assert items[0].quality == 50

    def test_quality_49_after_sell_date_capped_at_50(self):
        items = update([Item("Aged Brie", sell_in=0, quality=49)])
        assert items[0].quality == 50


# --- Sulfuras ---

class TestSulfuras:
    def test_quality_never_changes(self):
        items = update([Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)])
        assert items[0].quality == 80

    def test_sell_in_never_changes(self):
        items = update([Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)])
        assert items[0].sell_in == 0

    def test_quality_unchanged_when_sell_in_negative(self):
        items = update([Item("Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)])
        assert items[0].quality == 80


# --- Backstage passes ---

class TestBackstagePasses:
    NAME = "Backstage passes to a TAFKAL80ETC concert"

    def test_quality_increases_by_1_when_sell_in_above_10(self):
        items = update([Item(self.NAME, sell_in=15, quality=20)])
        assert items[0].quality == 21

    def test_sell_in_11_increases_by_1(self):
        items = update([Item(self.NAME, sell_in=11, quality=20)])
        assert items[0].quality == 21

    def test_quality_increases_by_2_when_sell_in_10(self):
        items = update([Item(self.NAME, sell_in=10, quality=20)])
        assert items[0].quality == 22

    def test_quality_increases_by_2_when_sell_in_6(self):
        items = update([Item(self.NAME, sell_in=6, quality=20)])
        assert items[0].quality == 22

    def test_quality_increases_by_3_when_sell_in_5(self):
        items = update([Item(self.NAME, sell_in=5, quality=20)])
        assert items[0].quality == 23

    def test_quality_increases_by_3_when_sell_in_1(self):
        items = update([Item(self.NAME, sell_in=1, quality=20)])
        assert items[0].quality == 23

    def test_quality_drops_to_0_after_concert(self):
        items = update([Item(self.NAME, sell_in=0, quality=20)])
        assert items[0].quality == 0

    def test_sell_in_decreases(self):
        items = update([Item(self.NAME, sell_in=5, quality=20)])
        assert items[0].sell_in == 4

    def test_quality_capped_at_50_in_normal_range(self):
        items = update([Item(self.NAME, sell_in=15, quality=50)])
        assert items[0].quality == 50

    def test_quality_capped_at_50_when_sell_in_10(self):
        items = update([Item(self.NAME, sell_in=10, quality=49)])
        assert items[0].quality == 50

    def test_quality_capped_at_50_when_sell_in_5(self):
        items = update([Item(self.NAME, sell_in=5, quality=49)])
        assert items[0].quality == 50

    def test_quality_capped_at_50_when_sell_in_5_quality_48(self):
        items = update([Item(self.NAME, sell_in=5, quality=48)])
        assert items[0].quality == 50


# --- Conjured items ---

class TestConjuredItems:
    def test_quality_decreases_by_2(self):
        items = update([Item("Conjured Mana Cake", sell_in=10, quality=10)])
        assert items[0].quality == 8

    def test_sell_in_decreases(self):
        items = update([Item("Conjured Mana Cake", sell_in=10, quality=10)])
        assert items[0].sell_in == 9

    def test_quality_decreases_by_4_after_sell_date(self):
        items = update([Item("Conjured Mana Cake", sell_in=0, quality=10)])
        assert items[0].quality == 6

    def test_quality_never_goes_below_0(self):
        items = update([Item("Conjured Mana Cake", sell_in=10, quality=1)])
        assert items[0].quality == 0

    def test_quality_never_goes_below_0_after_sell_date(self):
        items = update([Item("Conjured Mana Cake", sell_in=0, quality=3)])
        assert items[0].quality == 0
