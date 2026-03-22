import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def meet(): click.echo('Webex meeting')
@cli.command()
def message(): click.echo('Webex message')
if __name__ == '__main__': cli()
