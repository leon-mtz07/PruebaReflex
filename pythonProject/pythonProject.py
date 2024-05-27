"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.button(
                "Decrement",
                color_scheme="red",
                on_click=State.decrement,
            ),
            rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment",
                color_scheme="blue",
                on_click=State.increment,
            ),
            spacing="4",
        ))


app = rx.App()
app.add_page(index)
