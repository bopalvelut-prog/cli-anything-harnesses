import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('girl running')
@cli.command()
def start(): click.echo('girl started')
if __name__ == '__main__': cli()
