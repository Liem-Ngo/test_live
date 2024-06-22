from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", 1, 100, 50),
    ui.output_text("txt")
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n: {input.n()}"


app = App(app_ui, server)
