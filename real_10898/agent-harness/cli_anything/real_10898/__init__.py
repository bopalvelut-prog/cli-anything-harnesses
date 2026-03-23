import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('real_10898 running')
@cli.command()
def start(): click.echo('real_10898 started')
if __name__ == '__main__': cli()
