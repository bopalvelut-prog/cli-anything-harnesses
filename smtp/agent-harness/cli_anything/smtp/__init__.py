import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('smtp running')
@cli.command()
def start(): click.echo('smtp started')
if __name__ == '__main__': cli()
