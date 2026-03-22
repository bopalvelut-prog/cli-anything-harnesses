import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def streams(): click.echo('Zulip streams')
@cli.command()
def send(): click.echo('Zulip message')
if __name__ == '__main__': cli()
