import click
@click.group()
def cli(): pass
@cli.command()
def run(): click.echo('Ollama run')
@cli.command()
def list(): click.echo('Ollama list')
if __name__ == '__main__': cli()
