import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nextjs_v4 running')
@cli.command()
def start(): click.echo('nextjs_v4 started')
if __name__ == '__main__': cli()
