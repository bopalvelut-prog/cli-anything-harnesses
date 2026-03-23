import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('TextGen start')
@cli.command()
def models(): click.echo('TextGen models')
if __name__ == '__main__': cli()
