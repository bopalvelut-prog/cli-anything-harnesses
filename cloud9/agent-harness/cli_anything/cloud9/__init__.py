import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cloud9 running')
@cli.command()
def start(): click.echo('cloud9 started')
if __name__ == '__main__': cli()
