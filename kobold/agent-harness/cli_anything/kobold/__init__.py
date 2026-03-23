import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('KoboldAI start')
@cli.command()
def models(): click.echo('KoboldAI models')
if __name__ == '__main__': cli()
