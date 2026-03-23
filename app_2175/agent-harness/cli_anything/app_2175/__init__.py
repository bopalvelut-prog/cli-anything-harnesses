import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_2175 running')
@cli.command()
def start(): click.echo('app_2175 started')
if __name__ == '__main__': cli()
