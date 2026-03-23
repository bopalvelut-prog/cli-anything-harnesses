import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chezmoi running')
@cli.command()
def start(): click.echo('chezmoi started')
if __name__ == '__main__': cli()
