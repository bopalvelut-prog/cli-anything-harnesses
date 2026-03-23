import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fontconfig running')
@cli.command()
def start(): click.echo('fontconfig started')
if __name__ == '__main__': cli()
