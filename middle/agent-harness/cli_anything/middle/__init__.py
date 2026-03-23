import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('middle running')
@cli.command()
def start(): click.echo('middle started')
if __name__ == '__main__': cli()
