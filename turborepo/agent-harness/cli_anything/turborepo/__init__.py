import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_2183 running')
@cli.command()
def start(): click.echo('app_2183 started')
if __name__ == '__main__': cli()
