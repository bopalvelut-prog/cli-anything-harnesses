import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wagon running')
@cli.command()
def start(): click.echo('wagon started')
if __name__ == '__main__': cli()
