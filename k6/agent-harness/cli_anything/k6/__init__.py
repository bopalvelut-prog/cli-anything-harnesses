import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('k6 running')
@cli.command()
def start(): click.echo('k6 started')
if __name__ == '__main__': cli()
