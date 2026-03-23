import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('x86_64 running')
@cli.command()
def start(): click.echo('x86_64 started')
if __name__ == '__main__': cli()
