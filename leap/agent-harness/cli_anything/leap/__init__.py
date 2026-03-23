import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('leap running')
@cli.command()
def start(): click.echo('leap started')
if __name__ == '__main__': cli()
