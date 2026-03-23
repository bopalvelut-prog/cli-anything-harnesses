import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('m1 running')
@cli.command()
def start(): click.echo('m1 started')
if __name__ == '__main__': cli()
