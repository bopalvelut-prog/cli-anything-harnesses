import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('LocalAI start')
@cli.command()
def models(): click.echo('LocalAI models')
if __name__ == '__main__': cli()
