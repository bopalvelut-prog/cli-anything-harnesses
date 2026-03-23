import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('real_app_5177 running')
@cli.command()
def start(): click.echo('real_app_5177 started')
if __name__ == '__main__': cli()
