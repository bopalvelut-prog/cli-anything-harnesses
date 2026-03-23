import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('high running')
@cli.command()
def start(): click.echo('high started')
if __name__ == '__main__': cli()
