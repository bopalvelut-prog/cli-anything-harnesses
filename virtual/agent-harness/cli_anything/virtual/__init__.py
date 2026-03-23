import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('virtual running')
@cli.command()
def start(): click.echo('virtual started')
if __name__ == '__main__': cli()
