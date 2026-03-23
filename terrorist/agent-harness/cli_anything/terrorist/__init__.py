import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('terrorist running')
@cli.command()
def start(): click.echo('terrorist started')
if __name__ == '__main__': cli()
