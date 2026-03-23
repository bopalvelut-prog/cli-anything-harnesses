import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rasa running')
@cli.command()
def start(): click.echo('rasa started')
if __name__ == '__main__': cli()
