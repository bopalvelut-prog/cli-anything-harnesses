import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_2245 running')
@cli.command()
def start(): click.echo('app_2245 started')
if __name__ == '__main__': cli()
