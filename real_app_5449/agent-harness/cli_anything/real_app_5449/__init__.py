import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('real_app_5449 running')
@cli.command()
def start(): click.echo('real_app_5449 started')
if __name__ == '__main__': cli()
