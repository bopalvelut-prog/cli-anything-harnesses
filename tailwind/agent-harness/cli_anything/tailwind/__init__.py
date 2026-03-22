import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def build(): subprocess.run(['npx', 'tailwindcss', '-i', 'input.css', '-o', 'output.css'])
@cli.command()
def watch(): subprocess.run(['npx', 'tailwindcss', '-i', 'input.css', '-o', 'output.css', '--watch'])
@cli.command()
def init(): subprocess.run(['npx', 'tailwindcss', 'init'])
if __name__ == '__main__': cli()
