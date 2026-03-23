import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('real_10830 running')
@cli.command()
def start(): click.echo('real_10830 started')
if __name__ == '__main__': cli()
